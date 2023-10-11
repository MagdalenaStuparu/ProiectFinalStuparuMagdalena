Numele meu este Stuparu Magdalena si in cadrul acestui proiect am testat site-ul: https://automationexercise.com/.
Pentru a testa aceasta aplicatie web am folosit Libraria Unittest.

Am testat paginile de contact si pagina de Login atat cu un user nou cat si cu un user deja existent.
Pentru a testa aceste pagini mai intai am importat unittest si selenium apoi webdriver-ul pt browser.
Am creat clasa class Test2(unittest.TestCase): in cadrul careia am creat toate variabilele necesare pt a implementa testele.
Am implementata functiile:
def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://automationexercise.com/')
        self.chrome.implicitly_wait(5)


    def tearDown(self):
        self.chrome.quit()

Apoi am definit toate functiile necesare pt testarea acestor pagini.

Pentru a putea rula testele implementate trebuie sa avem instalat PyCharm si browserul Chrome.

Testele se pot rula  individual din fisierul proiect_final sau toate testele din fisierul suita_de_teste.

