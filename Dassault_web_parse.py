import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def Extract_Job_card(url):
    # JOB ID in the Dassault systeme Career Portal
    hashmap = ['firstcard', 'card-1', 'card-2', 'card-3', 'card-4',
               'card-5', 'card-6', 'card-7', 'card-8', 'card-9']

    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    username = ""  # your username
    password = ""  # your password
    driver = webdriver.Chrome(
        r"Path of your chrome drive", options=option)
    driver.get(url)
    driver.find_element(
        By.XPATH, '//*[@id="footer_tc_privacy_button_3"]').click()  # Cookie Accept
    time.sleep(3)

# //*[@id="dsjobsearch"]/div[5]/div/div[2]  //*[@id="dsjobsearch"]/div[5]/div/div[3]   //*[@id="dsjobsearch"]/div[5]/div/div[4]  //*[@id="dsjobsearch"]/div[5]/div/div[5]
    i = 0
    while len(hashmap) > i:
        driver.switch_to.window(driver.window_handles[0])
        print(f"Value of i={hashmap[i]}")
        # Click on Job JD
        driver.find_element(
            By.XPATH, f'//*[@id="{hashmap[i]}"]/div[2]/div[2]').click()

        ## JOB ID FINDING##############################
        time.sleep(3)
        job_id = driver.find_element(By.CLASS_NAME, 'job-details-id').text
        check = open("check.txt", 'a')
        with open("check.txt", 'r') as file:
            content = file.read()
            if job_id not in content:

                check.write(f"{job_id}\n")
                check.close()
                print(driver.title)
                time.sleep(5)

                driver.find_element(
                    By.XPATH, '//*[@id="dsjobsearch"]/div[3]/div[2]/div[5]/a').click()  # Click on Apply
                # //*[@id="dsjobsearch"]/div[3]/div[2]/div[5]/a
                # //*[@id="dsjobsearch"]/div[3]/div[2]/div[5]/a
                print("Clicked on Apply")
                time.sleep(10)
                driver.switch_to.window(driver.window_handles[1])
                # New Tab Open.
                print("New TAB opened !!")
                print(driver.title)
                try:
                    driver.find_element(
                        By.XPATH, '//*[@id="footer_tc_privacy_button_3"]').click()
                    time.sleep(3)
                except:
                    driver.find_element(
                        By.XPATH, '//*[@id="dialogTemplate-dialogForm-login-name1"]').send_keys(username)
                    print("Username Adding")
                    driver.find_element(
                        By.XPATH, '//*[@id="dialogTemplate-dialogForm-login-password"]').send_keys(password)
                    print("Password Adding")
                    time.sleep(3)
                    driver.find_element(
                        By.XPATH, '//*[@id="dialogTemplate-dialogForm-login-defaultCmd"]').click()
                    time.sleep(5)
                    print("Successfully logged In")
                    try:
                        driver.find_element(
                            By.XPATH, '//*[@id="et-ef-content-flowTemplate-LegalDisclaimerPage-legalDisclaimerContinueButton"]').click()
                        print("Privacy Accepted")
                        time.sleep(5)
                        driver.find_element(
                            By.XPATH, '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
                        time.sleep(3)
                        # Gender Select
                        driver.find_element(
                            By.XPATH, '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
                        time.sleep(3)
                        # File Select
                        driver.find_element(
                            By.XPATH, '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9:1:selectionid"]').click()
                        # //*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9:1:selectionid"]
                        print("File marked")
                        time.sleep(2)
                        driver.find_element(
                            By.XPATH, '//*[@id="editTemplateMultipart-editForm-content-ftf-saveContinueCmdBottom"]').click()

                        time.sleep(5)
                        driver.find_element(
                            By.XPATH, '//*[@id="et-ef-content-ftf-submitCmdBottom"]').click()

                        print("Successfully Submitted Gajanan")
                        time.sleep(3)
                    except:
                        try:
                            # Name select
                            driver.find_element(
                                By.XPATH, '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
                            time.sleep(3)
                            # Gender Select
                            driver.find_element(
                                By.XPATH, '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
                            time.sleep(3)
                            # File Select
                            driver.find_element(
                                By.XPATH, '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9:1:selectionid"]').click()
                            # //*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9:1:selectionid"]
                            print("File marked")
                            time.sleep(2)
                            driver.find_element(
                                By.XPATH, '//*[@id="editTemplateMultipart-editForm-content-ftf-saveContinueCmdBottom"]').click()

                            time.sleep(5)
                            driver.find_element(
                                By.XPATH, '//*[@id="et-ef-content-ftf-submitCmdBottom"]').click()

                            print("Successfully Submitted Gajanan")
                            time.sleep(3)
                        except:
                            try:  # Gender Select
                                driver.find_element(
                                    By.XPATH, '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]').click()
                                time.sleep(3)
                                # file Check
                                driver.find_element(
                                    By.XPATH, '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9:1:selectionid"]').click()

                                print("File marked")
                                time.sleep(2)

                                driver.find_element(
                                    By.XPATH, '//*[@id="editTemplateMultipart-editForm-content-ftf-saveContinueCmdBottom"]').click()

                                time.sleep(5)

                                driver.find_element(
                                    By.XPATH, '//*[@id="et-ef-content-ftf-submitCmdBottom"]').click()

                                print("Successfully Submitted Gajanan")
                                time.sleep(3)
                            except:
                                try:

                                    # file Check
                                    driver.find_element(
                                        By.XPATH, '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9:1:selectionid"]').click()

                                    print("File marked")
                                    time.sleep(2)

                                    driver.find_element(
                                        By.XPATH, '//*[@id="editTemplateMultipart-editForm-content-ftf-saveContinueCmdBottom"]').click()

                                    time.sleep(5)

                                    driver.find_element(
                                        By.XPATH, '//*[@id="et-ef-content-ftf-submitCmdBottom"]').click()

                                    print("Successfully Submitted Gajanan")
                                    time.sleep(3)
                                except:

                                    driver.find_element(
                                        By.XPATH, '//*[@id="et-ef-content-ftf-submitCmdBottom"]').click()

                                    print("Successfully Submitted Gajanan")

                    driver.find_element(
                        By.XPATH, '//*[@id="et-ef-content-flowTemplate-flowHeader-logoutAction"]').click()
                    print("LOGGED OUT")
                    time.sleep(5)
                    i += 1
                    driver.close()
            else:
                i += 1

            print("Switching to Back TAB")
            time.sleep(3)


Extract_Job_card(
    'https://www.3ds.com/careers/jobs?woc=%7B%22country%22%3A%5B%22country%2Findia%22%5D%7D')
