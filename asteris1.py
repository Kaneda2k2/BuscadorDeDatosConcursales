#-------------------------------------------------------------------------------
# Name:        Asteris1
# Purpose:     Rascar datos de la web seleccionada
#
# Author:      Kaneda2k2
#
# Created:     12/06/2021
# Copyright:   (c) ###
# Version:     1.2
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#libreria para crear arrays mediante argvs donde argvs[0] es el nombre del programa
import sys
from numpy import True_, append, result_type
#libreria para manejar el driver automanta  en este caso sera el geekodriver. tiene que estar dentro de  la propia carpeta
from selenium import webdriver
#funcion para los sleeps
import time
import pickle
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import action_chains
#funcion para la linea de comandos
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import is_connectable
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#libreria para crear instrucciones enm la linea de comandos.
import pandas as pd
#rom tabulate import tabulate
from selenium.webdriver import ActionChains
import csv
def update_csv_file():
        csv_writer = csv.writer(open('record1.csv','a'), delimiter='\t')
        csv_writer.writerow([[i],cif,ndeudor,njuez,njuzgado,nprocedimiento,cmediador,planliquidacion])

#################UTILES#################
#BAJAR EL SCROLL
#driver.execute_script("window.scrollTo(0,450);")
#MANDAR VARIABLES O TECLADO
#elem.send_keys()
#######################################################################
########################PANDA ABIERTO CON LOS DATOS PARA ITINERAR###########################
data = pd.read_csv(r'C:\xampp\htdocs\manejodecsv\record.csv',sep='\t') # INPUT DEL FICHERO
data1 = pd.read_csv(r'C:\xampp\htdocs\manejodecsv\record1.csv',sep='\t') # OUTPUT DEL FICHERO
#######################################################################
########################BUSCADOR INICIAL###########################
url='https://www.publicidadconcursal.es/concursal-web/afectado/buscar'
botonintroducircif="identificador"
clickbusqueda="search-button"

#driver.find_element_by_id(clickbusqueda).click()
#elem = driver.find_element_by_name(botonintroducircif)
tablaResultado="//td[@class=' center']"
#"/html/body/div[2]/section/div[1]/div/table/tbody/tr"
#driver.find_element_by_xpath("//td[@class=' center']").click()
#assert "publicaciones" in driver.title

#######################################################################
########################VARIABLES###########################
#ndeudor="//*[@class='col-md-7 item-content']"
#driver.find_element_by_xpath("//*[@class='col-md-7 item-content']").text
numerocif="//*[@class='col-md-2 item-content']"
#driver.find_element_by_xpath("//*[@class='col-md-2 item-content']").text
njuez="//*[@class='col-md-10 item-content']"
#driver.find_element_by_xpath("//*[@class='col-md-10 item-content']").text
njuzgado="//*[@class='col-md-6 item-content']"
#driver.find_element_by_xpath("//*[@class='col-md-6 item-content']").text
nujuzgado="//*[@class='col-sm-3 item-content']"
#driver.find_element_by_xpath("//*[@class='col-sm-3 item-content']").text
nprocedimiento="//*[@class='col-md-3 item-content']"
#driver.find_element_by_xpath("//*[@class='col-md-3 item-content']").text
cmediador="/html/body/div[2]/section/div/div[4]/div[1]/div[1]/div[4]"
#driver.find_element_by_xpath("/html/body/div[2]/section/div/div[4]/div[1]/div[1]/div[4]").text
planliquidacion = "//*[@class='col-sm-12 item-content-large-text']"
#driver.find_element_by_xpath("//*[@class='col-sm-12 item-content-large-text']").text
#######################################################################
########################LOS SITIOS DE BUSQUEDA###########################
autoDeclaracionConcurso='//*[contains(text(), "Auto de declaración de concurso")]'
#driver.find_element_by_xpath('//*[contains(text(), "Auto de declaración de concurso")]').click()
nombramientoConcursal='//td[contains(text(), "Nombramiento de Administrador concursal")]'
#driver.find_element_by_xpath('//td[contains(text(), "Nombramiento de Administrador concursal")]')
autoAprobacionLiquidacion='//td[contains(text(), "Auto de aprobación del plan de liquidación")]'
#driver.find_element_by_xpath('//td[contains(text(), "Auto de aprobación del plan de liquidación")]').click()
#######################################################################
########################ABRIMOS EL EXPLORADOR###########################
#driver = webdriver.Firefox()
#driver.get(url)
########################METEMOS EL BUCLE##########################


#abrimos el driver
##Reseteamos las variables
#ndeudor=""
#numerocif=""
#njuez=""
#njuzgado=""
#nprocedimiento=""
#cmediador=""
#planliquidacion=""



print("####### ASTERIS ####### EL INVENCIBLE ####### ")
print("####### VAMOS A RASCAR DATOS  ####### ")

####EMPEZAMOS
driver = webdriver.Firefox()
driver.get(url)
wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
time.sleep(1)
##ELIMINAMOS LAS COOKIES
elem = driver.find_element_by_xpath("/html/body/div[1]/p/a[1]").click()
if driver.title == "Búsqueda de publicaciones | Registro Público Concursal":
    print("####### ENTRAMOS EN LA WEB #######")
    print(data)
    print("####### ESTO ES LO QUE HAY QUE BUSCAR #######")
    print("####### DATA MINING ACTIVADO #######")
    
    

for row in data.itertuples():
        i=0
        if i <100:
            cif = row.Cif
        #####RESETEAMOS TODAS LAS VARIABLES
        ndeudor=""
        njuez=""
        njuzgado=""
        nprocedimiento=""
        cmediador=""
        planliquidacion=""
        #################   INTRODUCIMOS EL CIF DEL ARCHIVO DE ENTRADA   #################     
        elem = driver.find_element_by_name(botonintroducircif).clear()
        elem = driver.find_element_by_name(botonintroducircif)
        time.sleep(1)
        elem.send_keys(cif)
        time.sleep(1)
        driver.find_element_by_id(clickbusqueda).click()
        time.sleep(1)
        #################### SI DA POSITIVO ######################
        #################### COGE EL NUMERO DEL PROCEDIMIENTO ####
        try :
            time.sleep(1)
            elem12=driver.find_element_by_xpath("//td[@class=' center']").click()
            driver.execute_script("window.scrollTo(0,450);")
            nprocedimiento=driver.find_element_by_xpath('//td[contains(text(), "/")]').text
            
           
            print("NUMERO DE PROCEDIMIENTO ENCONTRADO")
            ############### AHORA ENTRA HA BUSCAR O AUTO,MEDIADOR,LIQUIDACION, O LAS TRES ########
            try:
                    driver.find_element_by_xpath('//*[contains(text(), "Auto de declaración de concurso")]').click
                    time.sleep(1)
                    elem =driver.find_element_by_xpath('//*[contains(text(), "Auto de declaración de concurso")]').click()
                    time.sleep(1)
                    
                   
                    ndeudor=driver.find_element_by_xpath("//*[@class='col-md-7 item-content' or @class='col-md-8 item-content']").text 
                    njuez=driver.find_element_by_xpath("//*[@class='col-md-10 item-content']").text
                    njuzgado=driver.find_element_by_xpath("//*[@class='col-sm-3 item-content' or @class='col-md-11 item-content']").text
                    
                    driver.back()
                    driver.execute_script("window.scrollTo(0,450);")
                    ############## AHORA ES MOMENTO DE VER SI HAY MEDIADOR #################


                    #########################################################
                    #driver.find_element_by_xpath('//td[contains(text(), "Nombramiento de Administrador concursal")]') .click()
                    try:
                            driver.find_element_by_xpath('//td[contains(text(), "Nombramiento de Administrador concursal")]').click()
                            print("#### ENTRAMOS EN EL NOMBRAMIENTO CONCURSAL ####")
                            driver.execute_script("window.scrollTo(0,450);")
                            time.sleep(5)  
                            cmediador=driver.find_element_by_xpath("/html/body/div[2]/section/div/div[4]/div[1]/div[1]/div[4]").text
                            driver.back()
                            time.sleep(1)
                            driver.execute_script("window.scrollTo(0,450);")
                            print("#### SALIMOS DEL NOMBRAMIENTO CONCURSAL ####")
                            try:
                                driver.execute_script("window.scrollTo(0,450);")
                                time.sleep(1)
                                driver.find_element_by_xpath('//td[contains(text(), "Auto de aprobación del plan de liquidación")]').click() 
                                print("#### ENTRAMOS EN EL PLAN DE LIQUIDACION ####")
                                driver.execute_script("window.scrollTo(0,450);")
                                planliquidacion= driver.find_element_by_xpath("//*[@class='col-sm-12 item-content-large-text']").text  
                                print("#### SALIMOS DEL PLAN DE LIQUIDACION ####")
                            except NoSuchElementException:
                                print("ELEMENTO TEST NO ENCONTRADO [1]")
                            finally:
                                print("#### ACTUALIZAMOS DATOS ####")
                                #update_csv_file()
                    except NoSuchElementException:
                        print("ELEMENTO TEST NO ENCONTRADO [2]")   
                    finally:
                        #update_csv_file()
                        print("")
            except NoSuchElementException:  
                    print("ELEMENTO TEST NO ENCONTRADO [3]")   
            finally:
                #########APLICAMOS EL NUEVO PARCHE############################

                try:
                    driver.find_element_by_xpath('//*[contains(text(), "Auto de declaración de concurso")]').click
                    time.sleep(1)
                    elem =driver.find_element_by_xpath('//*[contains(text(), "Auto de declaración de concurso")]').click()
                    time.sleep(1)
                    
                   
                    ndeudor=driver.find_element_by_xpath("//*[@class='col-md-7 item-content' or @class='col-md-8 item-content']").text 
                    njuez=driver.find_element_by_xpath("//*[@class='col-md-10 item-content' or @class='col-md-10 item-content' ]").text
                    njuzgado=driver.find_element_by_xpath("//*[@class='col-sm-3 item-content' or @class='col-md-11 item-content']").text
                    
                    driver.back()
                    driver.execute_script("window.scrollTo(0,450);")


                except NoSuchElementException:  
                    print("ELEMENTO TEST NO ENCONTRADO [4]")   
                finally:
                #########APLICAMOS EL NUEVO PARCHE############################
                    #update_csv_file()
                #########APLICAMOS EL NUEVO PARCHE############################
                    try:
                        driver.find_element_by_xpath('//td[contains(text(), "Nombramiento de Administrador concursal")]').click()
                        print("#### ENTRAMOS EN EL NOMBRAMIENTO CONCURSAL ####")
                        driver.execute_script("window.scrollTo(0,450);")
                        time.sleep(5)  
                        cmediador=driver.find_element_by_xpath("/html/body/div[2]/section/div/div[4]/div[1]/div[1]/div[4]").text
                        driver.back()
                        time.sleep(1)
                        driver.execute_script("window.scrollTo(0,450);")
                        print("#### SALIMOS DEL NOMBRAMIENTO CONCURSAL ####")
                        try:
                            driver.execute_script("window.scrollTo(0,450);")
                            time.sleep(1)
                            driver.find_element_by_xpath('//td[contains(text(), "Auto de aprobación del plan de liquidación")]').click() 
                            print("entramos en el plan de liquidacion")
                            driver.execute_script("window.scrollTo(0,450);")
                            planliquidacion= driver.find_element_by_xpath("//*[@class='col-sm-12 item-content-large-text']").text  
                                
                        except NoSuchElementException:
                            print("ELEMENTO TEST NO ENCONTRADO [5]")
                        finally:
                            print("na")
                            #update_csv_file()

                    except NoSuchElementException:
                        print("ELEMENTO TEST NO ENCONTRADO [6]")
                    finally:
                        print("na")
                        #update_csv_file()
                        #########APLICAMOS EL NUEVO PARCHE############################
                        try:
                            driver.execute_script("window.scrollTo(0,450);")
                            print("#### ENTRAMOS EN EL PLAN DE LIQUIDACION ####")
                            time.sleep(1)
                            driver.find_element_by_xpath('//td[contains(text(), "Auto de aprobación del plan de liquidación")]').click() 
                            print("entramos en el plan de liquidacion")
                            ndeudor=driver.find_element_by_xpath("//*[@class='col-md-7 item-content' or @class='col-md-8 item-content']").text 
                            time.sleep(1)
                            
                            driver.execute_script("window.scrollTo(0,450);")
                            planliquidacion= driver.find_element_by_xpath("//*[@class='col-sm-12 item-content-large-text']").text  
                            
                        except NoSuchElementException:
                            print("ELEMENTO TEST NO ENCONTRADO [7]")
                        finally:
                            print("na")
                            #update_csv_file()
                        continue
                ###########################################################
                update_csv_file()  
                #['Id','Busqueda','Resultado']
                time.sleep(1)
                    #driver.back()
                time.sleep(1)
                    #driver.quit()
                    #update_csv_file()
                driver.back()
                time.sleep(1)
                i=+1
                driver.back()
                elem = driver.find_element_by_name(botonintroducircif).clear()
                time.sleep(1) 
        except NoSuchElementException:  
            print("ELEMENTO TEST NO ENCONTRADO [8]")
        finally: 
            #['Id','Busqueda','Resultado']
            time.sleep(1)
            #driver.back()
            time.sleep(1)
            #driver.quit()
            #update_csv_file()
            update_csv_file()
            driver.back()
            time.sleep(1)
            i=i +1
            driver.back()
            elem = driver.find_element_by_name(botonintroducircif).clear()
            time.sleep(1)
                    



