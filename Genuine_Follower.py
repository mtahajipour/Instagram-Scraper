import pyodbc


server = 'localhost'
database = 'Sanjeh'
username = 'sa'
password = '1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cur = cnxn.cursor()
res=cur.execute('SELECT Follower,Follower_Count,Following_Count,Post_Count FROM [dbo].[Followers] WHERE LEN(Follower)>0')
F=res.fetchall()

min=-4
max=6
for x in F:
    try:
        F_Ratio=int(x[2])/int(x[1])
        if F_Ratio<=1:
            p=(F_Ratio-min)/(1-min)
            if p<0:
                p=0
        else:
            p=(F_Ratio-max)/(1-max)
            if p<0:
                p=0
        cursor = cnxn.cursor()
        cursor.execute('UPDATE [dbo].[Followers] SET PValue=? WHERE Follower=?',p,x[0])
        cnxn.commit()

    except:
        pass

curs = cnxn.cursor()
cnxn.close()
