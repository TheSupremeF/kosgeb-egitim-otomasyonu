import json
import os
from ast import Break
from gettext import find

from multiprocessing.connection import wait
from pickle import TRUE
from re import T
import time
from turtle import update
from webbrowser import get

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import winsound




import warnings
warnings.filterwarnings("ignore")


def kosgeb(username, password, target):
    
    driver = webdriver.Chrome()
    #driver.set_window_position(2000, 180)
    driver.get('https://lms.kosgeb.gov.tr/login/login_page/index.html')
    # wait for the page to load
    time.sleep(5)
    # find a href element
    driver.find_element_by_tag_name('a').click()
    # wait for the page to load
    time.sleep(5)
    # find the username field
    username_field = driver.find_element_by_name('tridField')
    # enter the username
    username_field.send_keys(username)
    # find the password field
    password_field = driver.find_element_by_name('egpField')
    # enter the password
    password_field.send_keys(password)
    # find the login button
    login_button = driver.find_element_by_class_name('submitButton')
    # click the login button
    login_button.click()
    # wait for the page to load
    time.sleep(15)

    if target == 1:
        lesson_id = 964
    elif target == 2:
        lesson_id = 990
    else:
        lesson_id = target

    #KURSU AÇAR
    while True:
        exit_to_lesson = False
        # go to lesson page
        driver.get('https://lms.kosgeb.gov.tr/course/view.php?id=' + str(lesson_id))
        # wait for the page to load
        time.sleep(10)
        # find the ul list
        ul = driver.find_element_by_id('multi_section_tiles')
        # find the li elements
        li_list = ul.find_elements_by_tag_name('li')
        li_list_url = ''
        for li_element in li_list:
            #print(li_element.get_attribute('class'))
            if 'tile tile-clickable' in li_element.get_attribute('class'):
                li_list_url = li_element.find_element_by_tag_name('a').get_attribute('href')
            elif 'tile tile-restricted' in li_element.get_attribute('class'):
                break

        #KİTAPCIGI AÇAR


        while True:
            driver.get(li_list_url)
            # wait for the page to load
            time.sleep(10)
            # find the ul list
            print('hi')

            go_out = False            

            content = driver.find_element_by_class_name('content')

            ul_course = content.find_element_by_tag_name('ul')
            # find the li elements
            li_list_courses = ul_course.find_elements_by_tag_name('li')



            for li_element_course in li_list_courses:

                if 'activity' in li_element_course.get_attribute('class'):

                    li_element_course_activity_span = li_element_course.find_element_by_class_name('actions')
                    for span in li_element_course_activity_span.find_elements_by_tag_name('span'):

                        if 'completioncheckbox' in span.get_attribute('class'):
                            if span.get_attribute('data-completionstate') == '0':
                                mod_indent = li_element_course.find_element_by_class_name('mod-indent-outer')
                                li_element_course_link = mod_indent.find_element_by_tag_name('a').get_attribute('href')
                                if 'modtype_resource' in li_element_course.get_attribute('class'):
                                    print('modtype_resource')
                                    li_element_course_type = 'modtype_resource'
                                    go_out = True
                                    break
                                elif 'modtype_page' in li_element_course.get_attribute('class'):
                                    print('modtype_page')
                                    li_element_course_type = 'modtype_page'
                                    go_out = True
                                    break
                                elif 'hvp modtype_hvp' in li_element_course.get_attribute('class'):
                                    print('hvp modtype_hvp')
                                    li_element_course_type = 'modtype_hvp'
                                    go_out = True
                                    break
                                elif 'modtype_quiz' in li_element_course.get_attribute('class'):
                                    print('modtype_quiz')
                                    li_element_course_type = 'modtype_quiz'
                                    go_out = True
                                    break
                if go_out:
                    break


        
                    

                            


            if li_element_course_type == 'modtype_resource':
                print('modtype_resource')
                driver.get(li_element_course_link)
                # wait for the page to load
                time.sleep(10)
                driver.get(li_list_url)
                break
            elif li_element_course_type == 'modtype_page':
                print('modtype_page')
                driver.get(li_element_course_link)
                # wait for the page to load
                time.sleep(10)
                driver.get(li_list_url)
                break
            elif li_element_course_type == 'modtype_quiz':
                print('modtype_quiz')
                driver.get(li_element_course_link)
                # wait for the page to load
                winsound.Beep(1000, 1000)
                input('Quiz açıldı. Devam etmek için enter tuşuna basınız.')
                driver.get(li_list_url)
                break
            elif li_element_course_type == 'modtype_hvp':
                print('modtype_hvp')
                driver.get(li_element_course_link)
                # wait for the page to load
                time.sleep(10)
                link = driver.execute_script("return H5PIntegration['ajax']['setFinished']+'&score=1&maxScore=1';")
                lesson_id = li_element_course_link[-4:]
                driver.get(f'{link}')
                # wait for the page to load
                time.sleep(5)
                exit_to_lesson = True

                break

            if exit_to_lesson:
                break


