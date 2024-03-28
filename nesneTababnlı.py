#Sorular -Questions

class Questions:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self,answer):
        return self.answer == answer 
        #içeride tanımladıgımız answer değeri ile dışardan gelen answer yani cevap eşitse dışarıya true degeri göndericek    
 





#Quiz classı oluşturucaz.

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
        #soru kısmında listeyi en baştan başlatmayı sağlıyacak
    def getQuestions(self):
        return self.questions[self.questionIndex]
        #burda da sorular içerisinden soru indeksini alma işlemi yapmış olucaz 
    
    def displayQuestion(self):
        question = self.getQuestions()
        #Burda ise yukarda tanımladıgımız fonskiyon içerisindeki soru indeksini çağırıp qestiona tanımladık
        print(f'Soru {self.questionIndex + 1}:{question.text}')
        #Burda 1.ci soru demek için indeksi 0 değilde 1 göstersin diye +1 verdik ve soru içeriğini gösterebilmek için .text tanımladık.
        
        for q in question.choices:
            print('-'+ q)
            #tire koyma maksatımız seçenekleri göster alt alta yanlarına - çek demektir
            
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()
        
    def guess(self,answer):
        question = self.getQuestions()
        
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
            
    def showScore(self):
        print('Score:',self.score)
        
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))
            
        
           
q1 = Questions('En iyi programlama dili hangisidir ?',['C#','python','javascript','C++'],'python') #seçenekler içerisinden python doğru cevap olacak bizim içiin       
q2 = Questions('En popüler programlama dili hangisidir ?',['Php','python','C#','java'],'python') 
q3= Questions('En çok kazandıran programlama dili hangisidir ?',['NodeJs','python','Html','java'],'python') 
q4= Questions('En çok sevilen programlama dili hangisidir ?',['C#','python','Flask','Django'],'python') 
q5= Questions('En kolay programlama dili hangisidir ?',['Angular','python','Css','React'],'python') 

questions =[q1,q2,q3,q4,q5]
    
quiz = Quiz(questions)

quiz.loadQuestion()

'''
Questions (Sorular) Sınıfı:

__init__ metodu: Soru metni (text), seçenekler (choices), doğru cevap (answer) parametreleriyle oluşturulur.
checkAnswer metodu: 
Alınan cevabın doğru olup olmadığını kontrol eder. Doğru ise True döndürür.

Quiz (Test) Sınıfı
__init__ metodu: 
Soruların listesi (questions), skor (score), şu anki soru indeksi (questionIndex) gibi özellikleri tanımlar.

getQuestions metodu: 
Mevcut soruyu alır ve döndürür.

displayQuestion metodu: 
Mevcut soruyu ekrana yazar ve cevabı kullanıcıdan alır. 
Ardından guess ve loadQuestion metodlarını çağırarak işlemleri yönetir.

guess metodu: 
Kullanıcının cevabını kontrol eder ve doğru ise skoru artırır, sonra soru indeksini bir artırır.

loadQuestion metodu: 
Soru sayısı ile şu anki soru indeksini karşılaştırarak 
sıradaki işlemi belirler. 
Eğer tüm sorular sorulduysa skoru gösterir, 
aksi takdirde sıradaki soruyu gösterir.

showScore metodu: Toplam skoru ekrana yazdırır.
displayProgress metodu: Quiz ilerlemesini ekrana yazdırır.
Sorular:

Her bir soru, Questions sınıfından oluşturulur ve soru metni, seçenekler ve doğru cevap ile başlatılır.
Quiz Oluşturma ve Çalıştırma:

Quiz sınıfından bir quiz oluşturulur ve loadQuestion metodu çağrılarak quiz başlatılır.
Bu kod parçacığı, bir quiz uygulaması yapmak için kullanılır. İlk olarak Questions sınıfı, her bir soruyu temsil eder ve doğru cevabı kontrol etmek için bir metod içerir. Daha sonra Quiz sınıfı, bir dizi soruyu içeren bir obje alır ve kullanıcının cevaplarını kontrol ederek bir quiz yönetir. Quiz başladığında, her soru ekrana yazdırılır, kullanıcının cevabı alınır ve doğru olup olmadığı kontrol edilir. Quiz tamamlandığında, kullanıcının aldığı toplam skor görüntülenir.




'''
#BU KISIMDA TÜRKÇE KARAKTERLER KULLANILARAK YUKARDAKİ KODUN AYNI MANTIĞINDA YAZILDI.

#Sorular -Questions

class Sorular:
    def __init__(self, metin, secenekler, cevap):
        self.metin = metin
        self.secenekler = secenekler
        self.cevap = cevap
    
    def cevabiKontrolEt(self, cevap):
        return self.cevap == cevap


#Quiz sınıfını oluşturalım.

class Quiz:
    def __init__(self, sorular):
        self.sorular = sorular
        self.skor = 0
        self.soruIndeksi = 0
    
    def getSoru(self):
        return self.sorular[self.soruIndeksi]
    
    def soruyuGoster(self):
        soru = self.getSoru()
        print(f'Soru {self.soruIndeksi + 1}: {soru.metin}')
        
        for secenek in soru.secenekler:
            print('-' + secenek)
            
        cevap = input('Cevap: ')
        self.tahmin(cevap)
        self.soruyuYukle()
        
    def tahmin(self, cevap):
        soru = self.getSoru()
        
        if soru.cevabiKontrolEt(cevap):
            self.skor += 1
        self.soruIndeksi += 1
    
    def soruyuYukle(self):
        if len(self.sorular) == self.soruIndeksi:
            self.skoruGoster()
        else:
            self.ilerlemeDurumunuGoster()
            self.soruyuGoster()
            
    def skoruGoster(self):
        print('Skor:', self.skor)
        
    def ilerlemeDurumunuGoster(self):
        toplamSoru = len(self.sorular)
        soruNumarasi = self.soruIndeksi + 1
        
        if soruNumarasi > toplamSoru:
            print('Quiz bitti.')
        else:
            print(f'Soru {soruNumarasi} / {toplamSoru}'.center(100, '*'))


soru1 = Sorular('En iyi programlama dili hangisidir ?', ['C#', 'python', 'javascript', 'C++'], 'python')
soru2 = Sorular('En popüler programlama dili hangisidir ?', ['Php', 'python', 'C#', 'java'], 'python')
soru3 = Sorular('En çok kazandıran programlama dili hangisidir ?', ['NodeJs', 'python', 'Html', 'java'], 'python')
soru4 = Sorular('En çok sevilen programlama dili hangisidir ?', ['C#', 'python', 'Flask', 'Django'], 'python')
soru5 = Sorular('En kolay programlama dili hangisidir ?', ['Angular', 'python', 'Css', 'React'], 'python')

sorular = [soru1, soru2, soru3, soru4, soru5]
    
quiz = Quiz(sorular)

quiz.soruyuYukle()
