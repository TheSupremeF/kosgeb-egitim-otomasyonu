from ast import Break
from gettext import find
import json
import os
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

    target = 'geleneksel'

    driver = webdriver.Chrome()
    driver.set_window_position(2000, 180)
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
    time.sleep(10)

    if target == 'geleneksel':
        lesson_id = 964

    #KURSU AÇAR
    while True:
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
                continue
            elif li_element_course_type == 'modtype_page':
                print('modtype_page')
                driver.get(li_element_course_link)
                # wait for the page to load
                time.sleep(10)
                continue
            elif li_element_course_type == 'modtype_quiz':
                print('modtype_quiz')
                driver.get(li_element_course_link)
                # wait for the page to load
                winsound.Beep(1000, 1000)
                input('Quiz açıldı. Devam etmek için enter tuşuna basınız.')
                continue
            elif li_element_course_type == 'modtype_hvp':
                print('modtype_hvp')
                driver.get(li_element_course_link)
                # wait for the page to load
                time.sleep(10)
                #main_content = driver.find_element_by_id('main-content')
                #page_content = main_content.find_element_by_id('page-content')
                #h5p_iframe_wrapper = page_content.find_element_by_class_name('h5p-iframe-wrapper')
                driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
                h5p_video = driver.find_element_by_class_name('h5p-video')
                h5p_total = h5p_video.find_element_by_class_name('h5p-total')
                h5p_human_time = h5p_total.find_element_by_class_name('human-time').text
                h5p_human_time_split = h5p_human_time.split(':')
                h5p_human_time_split_minutes = h5p_human_time_split[0]
                h5p_human_time_split_seconds = h5p_human_time_split[1]
                calculated_time = int(h5p_human_time_split_minutes) * 60 + int(h5p_human_time_split_seconds) + 10
                print('calculated_time: ' + str(calculated_time))
                h5p_play = h5p_video.find_element_by_class_name('h5p-play')
                h5p_play.click()
                time.sleep(calculated_time)
                h5p_sc_label = driver.find_element_by_class_name('h5p-sc-label')
                h5p_sc_label.click()
                time.sleep(10)
                h5p_question_iv_continue = driver.find_element_by_class_name('h5p-question-iv-continue')
                h5p_question_iv_continue.click()
                time.sleep(5)
                h5p_joubelui_button = driver.find_element_by_class_name('h5p-joubelui-button')
                h5p_joubelui_button.click()
                time.sleep(5)
                driver.switch_to.default_content()
                continue
