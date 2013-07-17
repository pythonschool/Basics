#6-2-2012
#additional exercise 6
#sample solution

print("Quiz Program")
print("this program stores quiz questions and allows you to take the quiz")
print()
#empty list of quiz
quizQuestions = []

#enter questions
finished = False
while not finished:
    question = input("Please enter a question: ")
    if len(question) == 0:
        finished = True
    else:
        tempQuestionList = []
        tempQuestionList.append(question)
        answers = int(input("How many possible answers do you want this question to have: "))
        for each in range(answers):
            tempAnswer = input("Please enter the next answer: ")
            tempQuestionList.append(tempAnswer)
        print()
        #display answers
        for each in range(1,len(tempQuestionList)):
            print("{0}. {1}".format(each,tempQuestionList[each]))
        print()
        correctAnswer = int(input("Please enter the value of the correct answer: "))
        tempQuestionList.append(correctAnswer)
        #add question to the list
        quizQuestions.append(tempQuestionList)
#play the quiz
score = 0
questionNo = 0
for each in quizQuestions:
    #display question
    print()
    questionNo = questionNo + 1
    print("Question {0}. {1}?".format(questionNo,each[0]))
    print()
    print("Possible Answers: ")
    for ans in range(1,len(each)-1):
        print("{0}. {1}".format(ans,each[ans]))
    print()
    givenAnswer = int(input("Please select an answer: "))
    print(givenAnswer)
    print(each[len(each)-1])
    if givenAnswer == each[len(each)-1]:
        score = score + 1
        print("well done, you answered the question correctly!")
    else:
        print("sorry, you didn't get the correct answer.")
#display score
print()
print("Your final score was {0} out of {1}.".format(score,len(quizQuestions)))
    
        
    
    
