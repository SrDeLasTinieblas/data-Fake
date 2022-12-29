from faker import Faker
import pandas as pd 
import string
import random
import bcrypt
import os, binascii

def cadena():
    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        return(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

def encryptingCadena():
    pass_texto_plano = cadena()
    pass_texto_plano = pass_texto_plano.encode()
    sal = bcrypt.gensalt()

    # Hashear
    pass_hasheada = bcrypt.hashpw(pass_texto_plano, sal)
    encoding = 'utf-8'
    #s = str(b, encoding)
    #str(b, encoding)
    return str(pass_hasheada, encoding) + " ==>> " + cadena()

def apiKeyGenerator():
    apiKeyGenerator = binascii.b2a_hex(os.urandom(20))
    encoding = 'utf-8'
    return str(apiKeyGenerator, encoding)



fake = Faker()
#INSERT Usuarios (Usuario, Pass, Llave) values ('Tinieblas', 'darkangelo', '123456789') fake.name()
for _ in range( 10 ):                                    #Stephanie Allen          pass          
    print("INSERT Usuarios (Usuario, Pass, Llave) values ('" + fake.name() + "'," + " '"+ encryptingCadena() + "'," + "'" + apiKeyGenerator() + "')" )
    #print(fake.address)


## Generador de perfil falso con pandas
#generateProfile = Faker() 
#data = [generateProfile.profile() for i in range( 1000 )]
#print(pd.DataFrame(data)) 

#print(df.columns)
# generate 1000 profiles data = [generateProfile.profile() for i in range( 1000 )] # save profiles in pandas dataframe df = pd.DataFrame(data) print(df) 


