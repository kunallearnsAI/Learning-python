questions = [
    { 
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    { 
        "question": "Who is the first Prime minister of India?",
        "options": ["A. Dr.Rajendra prasad", "B. Dr.Jawahar lal nehru", "C. Dr.APJ kalam", "D. Indira Gandhi"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. H2o", "B. o2", "C. Co2", "D. Nacl"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Tokyo", "B. Seoul", "C. Beijing", "D. Bangkok"],
        "answer": "A"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    }
]

prize = [1000, 2000, 3000, 5000, 10000, 20000, 50000]
money = 0

for i in range(0, len(questions)):
    q = questions[i]
    print(f"\nQuestion for RS.{prize[i]}")
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    answer = input("Enter your answer (A/B/C/D): ")

    if answer == q["answer"]:
        print(" Correct answer!")
        money = prize[i]
    else:
        print(" Wrong answer!")
        print(f"You won RS {money}")
        break  


    
