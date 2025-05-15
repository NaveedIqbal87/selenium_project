# Selenium Pytest CI/CD Pipeline with Jenkins

This project demonstrates a complete CI/CD setup using:

- ✅ Selenium with Python (Pytest)
- ✅ Jenkins for Continuous Integration
- ✅ GitHub integration with SCM polling
- ✅ Allure reports for test results
- ✅ Browser drivers via WebDriverManager

### Jenkins Job Features
- SCM-triggered builds (GitHub push triggers Jenkins)
- Python environment setup
- Automated testing with `pytest`
- Allure test report generation
- Artifact archiving for test results

### Sample Test
```python
@pytest.mark.parametrize("username,password", my_credential())
def test_login(username, password):
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
