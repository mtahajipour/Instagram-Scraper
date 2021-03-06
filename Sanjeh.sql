USE [master]
GO
/****** Object:  Database [Sanjeh]    Script Date: 4/27/2019 1:47:48 PM ******/
CREATE DATABASE [Sanjeh]
GO
ALTER DATABASE [Sanjeh] SET COMPATIBILITY_LEVEL = 120
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Sanjeh].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Sanjeh] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Sanjeh] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Sanjeh] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Sanjeh] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Sanjeh] SET ARITHABORT OFF 
GO
ALTER DATABASE [Sanjeh] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Sanjeh] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Sanjeh] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Sanjeh] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Sanjeh] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Sanjeh] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Sanjeh] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Sanjeh] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Sanjeh] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Sanjeh] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Sanjeh] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Sanjeh] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Sanjeh] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Sanjeh] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Sanjeh] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Sanjeh] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Sanjeh] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Sanjeh] SET RECOVERY FULL 
GO
ALTER DATABASE [Sanjeh] SET  MULTI_USER 
GO
ALTER DATABASE [Sanjeh] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Sanjeh] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Sanjeh] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Sanjeh] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO
ALTER DATABASE [Sanjeh] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'Sanjeh', N'ON'
GO
USE [Sanjeh]
GO
/****** Object:  Table [dbo].[Comments]    Script Date: 4/27/2019 1:47:48 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Comments](
	[Post_URL] [nvarchar](50) NULL,
	[Comment] [nvarchar](500) NULL,
	[Person] [nvarchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Followers]    Script Date: 4/27/2019 1:47:48 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Followers](
	[Account] [nvarchar](50) NULL,
	[Follower] [nvarchar](50) NULL,
	[Post_Count] [int] NULL,
	[Follower_Count] [int] NULL,
	[Following_Count] [int] NULL,
	[PValue] [float] NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Following]    Script Date: 4/27/2019 1:47:48 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Following](
	[Account] [nvarchar](50) NULL,
	[Following] [nvarchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Popular_Hashtags]    Script Date: 4/27/2019 1:47:48 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Popular_Hashtags](
	[Keyword] [nvarchar](50) NULL,
	[Hashtags] [nvarchar](50) NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Posts]    Script Date: 4/27/2019 1:47:48 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Posts](
	[Post_URL] [nvarchar](100) NULL,
	[Post_Date] [datetime] NULL,
	[Like_Count] [int] NULL,
	[View_Count] [int] NULL
) ON [PRIMARY]

GO
USE [master]
GO
ALTER DATABASE [Sanjeh] SET  READ_WRITE 
GO
