user_score=float(input("Your score in Percentage: "))
if user_score>=93.33 and user_score<=100:
    print("Grade A")
if user_score>=90 and user_score<=93.33:
    print("Grade A-")
if user_score>=86.67 and user_score<=90:
    print("Grade B+")
if user_score>=83.33 and user_score<=86.67:
    print("Grade B")
if user_score>=80 and user_score<=83.33:
    print("Grade B-")
if user_score>=76.67 and user_score<=80:
    print("Grade C+")
if user_score>=73.33 and user_score<=76.67:
    print("Grade C")
if user_score>=70 and user_score<=73.33:
    print("Grade C-")
if user_score>=66.67 and user_score<=70:
    print("Grade D+")
if user_score>=63.33 and user_score<=66.67:
    print("Grade D")
if user_score>=60 and user_score<=63.33:
    print("Grade D-")
if user_score<60 and user_score>=0:
    print("Grade F")
if user_score>100 and user_score<0:
    print("Invalid Percentage.")