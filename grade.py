# Class to represent candidates and their scores
class CandidateScores:
    def __init__(aksh, name, score):
        aksh.name = name
        aksh.score = score
    
    def get_grade(aksh):
        if aksh.score >= 90:
            return "A"
        elif aksh.score >= 75:
            return "B"
        elif aksh.score >= 50:
            return "C"
        else:
            return "No Grade"

candidate1 = CandidateScores("Candidate 1", 92)
candidate2 = CandidateScores("Candidate 2", 78)
candidate3 = CandidateScores("Candidate 3", 48)

# Compare and display their grades
print("Scores and Grades of Candidates:")
for candidate in [candidate1, candidate2, candidate3]:
    print("{candidate.name}: Score = {candidate.score}, Grade = {candidate.get_grade()}")