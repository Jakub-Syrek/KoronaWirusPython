import pyodbc
import datetime 
from datetime import datetime
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=QB\QBMSSQLSERVER;'
                      'Database=CoronaVirusDB;'
                      'Trusted_Connection=yes;')
 
cursor = conn.cursor()
 
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

listaDzielona = list()
lista = list()

f = open(r"ConfirmedCasesPolskaDetails.txt","r",encoding="utf-8")   
for x in f:
    lista.append(str(x).rstrip())
    if is_integer(str(x).rstrip()):
        listaDzielona.append(str(x).rstrip())         

f.close()

cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_dolnośląskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES({listaDzielona[0]},{listaDzielona[1]},geography::Point(51.102957, 17.046622, 4326))
                ''')
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[0]}',{lista[1]},{lista[2]},geography::Point(51.102957, 17.046622, 4326))
               ''')



cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_kujawsko_pomorskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES 
                ({listaDzielona[2]},{listaDzielona[3]},geography::Point(53.041517, 18.592496, 4326))
                ''')
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[3]}',{lista[4]},{lista[5]},geography::Point(53.041517, 18.592496, 4326))
               ''')



cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_lubelskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[4]},{listaDzielona[5]},geography::Point(51.254097, 22.568101, 4326))
                ''')
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[6]}',{lista[7]},{lista[8]},geography::Point(51.254097, 22.568101, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_lubuskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[6]},{listaDzielona[7]},geography::Point(51.930345, 15.508407, 4326))
                ''')           
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[9]}',{lista[10]},{lista[11]},geography::Point(51.930345, 15.508407, 4326))
               ''')




cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_łódzkie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[8]},{listaDzielona[9]},geography::Point(51.759046, 19.454623, 4326))
                ''') 
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[12]}',{lista[13]},{lista[14]},geography::Point(51.759046, 19.454623, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_małopolskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[10]},{listaDzielona[11]},geography::Point(50.059172, 19.940370, 4326))
                ''') 
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[15]}',{lista[16]},{lista[17]},geography::Point(50.059172, 19.940370, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_mazowieckie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[12]},{listaDzielona[13]},geography::Point(52.242243, 20.995826, 4326))
                ''')           
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[18]}',{lista[19]},{lista[20]},geography::Point(52.242243, 20.995826, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_opolskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[14]},{listaDzielona[15]},geography::Point(50.692370, 17.930514, 4326))
                ''')
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[21]}',{lista[22]},{lista[23]},geography::Point(50.692370, 17.930514, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_podkarpackie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[16]},{listaDzielona[17]},geography::Point(50.034143, 22.015340, 4326))
                ''')    
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[24]}',{lista[25]},{lista[26]},geography::Point(50.034143, 22.015340, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_podlaskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[18]},{listaDzielona[19]},geography::Point(53.138419, 23.187679, 4326))
                ''')
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[27]}',{lista[28]},{lista[29]},geography::Point(53.138419, 23.187679, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_pomorskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[20]},{listaDzielona[21]},geography::Point(54.354466, 18.619139, 4326))
                ''')
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[30]}',{lista[31]},{lista[32]},geography::Point(54.354466, 18.619139, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_śląskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[22]},{listaDzielona[23]},geography::Point(50.255856, 19.023534, 4326))
                ''')
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[33]}',{lista[34]},{lista[35]},geography::Point(50.255856, 19.023534, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_świętokrzyskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[24]},{listaDzielona[25]},geography::Point(50.867632, 20.623915, 4326))
                ''')
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[36]}',{lista[37]},{lista[38]},geography::Point(50.867632, 20.623915, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_warmińsko_mazurskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[26]},{listaDzielona[27]},geography::Point(53.787235, 20.497471, 4326))
                ''')          
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[39]}',{lista[40]},{lista[41]},geography::Point(53.787235, 20.497471, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_wielkopolskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[28]},{listaDzielona[29]},geography::Point(52.434875, 16.880647, 4326))
                ''')
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[42]}',{lista[43]},{lista[44]},geography::Point(52.434875, 16.880647, 4326))
               ''')


cursor.execute(f'''
                INSERT INTO [dbo].[Koronawirus_Polska_zachodniopomorskie]
           ([Zarażeni]
           ,[Zgony]
           ,[Współrzędne])
           VALUES 
                ({listaDzielona[30]},{listaDzielona[31]},geography::Point(53.430652, 14.580189, 4326))
                ''')
cursor.execute(f'''
               INSERT INTO [dbo].[KoronawirusDane]
           ([Województwo]
           ,[Zarażeni]
           ,[Zgony]
           ,[Współrzędne])           
           VALUES
               ('{lista[45]}',{lista[46]},{lista[47]},geography::Point(53.430652, 14.580189, 4326))
               ''')
conn.commit()