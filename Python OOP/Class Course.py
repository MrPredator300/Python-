class Course:
     def __init__(self,title,instructor,lectures,price):
         self.title=title
         self.instructor=instructor
         self.lectures=lectures
         self.price=price
         self.users=[]
         self.rating=0
         self.avg_rating=0
        
    def __str__(self):
        return f'{self.title} by {self.instructor}'
    
    def new_user_enrolled(self,user):
        self.users.append(user)
    
    def recieved_a_rating(self,new_rating):
        self.avg_rating=(self.avg_rating + self.ratings + new_rating)/(self.ratings +1)
        self.rating+=1
    
    def show_details(self):
        print('Course Title :',self.title)
        print('Instructor :',self.instructor)
        print('Lectures :',self.lectures)
        print('Price :',self.price)
        print('Users :',self.users)
        print('Average Rating :',self.avg_rating)

class Videocourse(Course):
    def __init__(self, title, instructor, lectures, price, length_video):
        super().__init__(title, instructor, lectures, price)
        self.length_video=length_video

    def show_details(self):
        super().show_details()
        print('Video Length :',self.length_video)
    
class PdfCourse(Course):
    def __init__(self, title, instructor, lectures, price,pages):
        super().__init__(title, instructor, lectures, price)
        self.pages=pages
    
    def show_details(self):
        super().show_details()
        print('Number of pages :',self.pages)
    
vc=Videocourse('Learn C++','Bob',30,800,700)
vc.new_user_enrolled('Allen')
vc.new_user_enrolled('Alan')
vc.new_user_enrolled('Alice')
vc.recieved_a_rating(3)
vc.recieved_a_rating(4)
vc.recieved_a_rating(5)
vc.show_details()

print()

pc=PdfCourse('Learn Java','Jenny',45,900,2000)
pc.new_user_enrolled('Jack')
pc.new_user_enrolled('Molly')
pc.new_user_enrolled('Janice')
pc.recieved_a_rating(3.8)
pc.recieved_a_rating(4.3)
pc.recieved_a_rating(4.5)
pc.show_details()



    


         