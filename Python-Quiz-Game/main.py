def give_options(x, y, z):
    print("a):", x)
    print("b):", y)
    print("c):", z)

print("Hello! Welcome to my Quiz")
print("All Questions carry 10 marks each")

ans = input("Are you ready to play (yes/no): ")
note = "Note: Write answers! Do not write option letters."
score = 0
total_questions = 4

correct_answers = ["python", "steve jobs", "artificial intelligence", "bitcoin"]

if ans.lower() == "yes":
    print(note)
    
    print("\nQuestion - What is the best Programming Language?")
    give_options("Python", "C", "Java")
    ans = input(">>> ")
    if ans.lower() == correct_answers[0]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    print(note)
    print("\nQuestion - Who is the Founder of Apple Inc?")
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve Jobs")
    ans = input(">>> ")
    if ans.lower() == correct_answers[1]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    print(note)
    print("\nQuestion - What is better among these?")
    give_options("Data Science", "Artificial Intelligence", "Digital Marketing")
    ans = input(">>> ")
    if ans.lower() == correct_answers[2]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    print(note)
    print("\nQuestion - What is the best Investment?")
    give_options("Share Capital", "Mutual Funds", "Bitcoin")
    ans = input(">>> ")
    if ans.lower() == correct_answers[3]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    score_result = score * 10

    if score_result < 30:
        print(f"Oops, your score is {score_result}/40. Better luck next time.")
    elif score_result == 30:
        print(f"Wow! You scored {score_result}/40. You are quite smart.")
    else:
        print(f"Congratulations! It's a perfect {score_result}/40. You are Intelligent.")
else:
    print("Okay! See you next time.")