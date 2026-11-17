import time
import random

def check(user_input,text,time):
    c=user_input
    count=0
    i=0
    while i<len(c) and i<len(text):
        if (c[i]==text[i]):
            count+=1
            i+=1
        else:
            count=count
            i+=1
    accruacy=(count/len(text))*100
    word=len(c.split())
    speed=word/time
    print(f"your typing speed is {speed:.0f} words per min and accruacy is {accruacy:.2f}%")

list=["Early morning is often the most peaceful time of the day. The air feels fresh, and the world seems quieter compared to the usual noise of daily life. Many people use this time to exercise, read, or simply think about their goals. The soft light of the rising sun creates a calm atmosphere that helps the mind focus better. Starting the day early can improve productivity and bring a sense of control over one’s schedule. Even a short walk or a few minutes of silence can make a noticeable difference. It prepares the mind and body to handle the challenges of the day.","Learning to manage time effectively is an important skill for students and professionals alike. Without proper planning, tasks can quickly pile up and create unnecessary stress. Making a simple schedule or to-do list helps in organizing daily activities. It allows you to prioritize important work and avoid last-minute pressure. Taking short breaks between tasks can also improve focus and efficiency. Over time, good time management becomes a habit that increases productivity and reduces anxiety. It also gives more free time to relax or pursue hobbies. A balanced routine leads to a more disciplined and satisfying life.","Reading books is one of the best ways to gain knowledge and improve thinking ability. It helps in developing vocabulary and enhances imagination. Whether it is fiction or non-fiction, every book offers something valuable. Reading regularly also improves concentration and reduces stress. In a world full of digital distractions, picking up a book can feel refreshing and calming. It allows you to explore new ideas and perspectives. Even spending a few minutes each day reading can create a positive habit. Over time, this habit can lead to personal growth and a deeper understanding of different subjects.","Physical fitness plays a crucial role in maintaining overall health. Regular exercise not only keeps the body active but also improves mental well-being. Activities like walking, running, or playing sports help in building strength and stamina. Exercise also releases chemicals in the brain that reduce stress and improve mood. Maintaining a healthy diet along with exercise is equally important. Small changes, like drinking enough water and avoiding junk food, can make a big difference. Staying fit increases energy levels and helps in performing daily tasks more efficiently. A healthy lifestyle leads to a longer and happier life.","Technology has changed the way people live and work. It has made communication faster and more convenient. With the help of the internet, information is available instantly. Students can learn new skills online, and professionals can work from anywhere. However, excessive use of technology can also lead to distractions. Spending too much time on mobile devices may affect productivity and health. It is important to use technology wisely and maintain a balance. Taking breaks from screens and engaging in offline activities is necessary. When used properly, technology can be a powerful tool for growth and success."]
t=random.randint(0,4)
print(list[t])
x=input("Write the text showing above press 'Enter' to start typing:")
st=time.time()
y=input("=>")
et=time.time()
total_time=(et-st)
time_in_min=total_time/60
check(y,list[t],time_in_min)
print(f"You typed the above text in {total_time:.2f} seconds")
