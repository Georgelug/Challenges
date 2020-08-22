'''
Cody has sequence of characters N.
He likes a sequence if it contains his favourite sequence as a substring.
Given the sequence and his favourite sequence F, check whether the favourite sequence F, check whether the favourite sequence is present in the sequence.

'''
class StringMatching:
    def __init__(self,N,F):
        self.N = N
        self.F = F
    def __Stringsubstring(self):
        return self.F in self.N
    def ShowResults(self):
        if self.__Stringsubstring():
            return "Yes"
        return "No"

if __name__ == "__main__":
    Cody = StringMatching(input("\nN: "),input("\nF: "))
    print(Cody.ShowResults())