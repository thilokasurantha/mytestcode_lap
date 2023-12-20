class CalculatorProgramme :
    def __init__(self, user) -> None:
        self.user = user

    def checking_numbers(self, ):
        self.l = [chr(ord('a') + i) for i in range(26)]
        self.u = [chr(ord('A') + i) for i in range(26)]
        nums = self.l+self.u
        res1 = []
        for check_num in self.user :
            for check_l_nums in nums :
                if check_l_nums not in check_num :
                    res1.append(True)

                else :
                    res1.append(False)
                    return False
                
        if res1[0] :
            self.check_operators()
        
        else :
            None


    def check_operators(self, ):
        operators = ["+", "-", "*", "/", "//", "**"]
        self.algo_operator = ["(", ")"]
        if "(" in self.user :
            self.bracketing(self.algo_operator)

        else :
            self.nan_claculations()

    def bracketing(self, ope):
        self.ope = ope
        self.fow_bracket = []
        self.back_bracket = []
        for f_b in range(0, len(self.user)) :
            if self.algo_operator[0] in self.user[f_b] :
                self.fow_bracket.append(f_b)
            if  self.algo_operator[1] in self.user[f_b] :
                self.back_bracket.append(f_b)
        cur=0
        dis=1
        back_dub = set({})
        while(dis<len(self.back_bracket)) :
            if self.back_bracket[dis] == self.back_bracket[cur]+1 :
                back_dub.add(cur)
                back_dub.add(dis)
                cur+=1
                dis+=1
            
            else :
                cur+=1
                dis+=1
        back_dub = list(back_dub)
        self.dub = []
        cur=0
        dis=1
        while(dis<len(back_dub)) :
            if back_dub[dis] == back_dub[cur]+1 :
                self.dub.append([self.back_bracket[back_dub[cur]], self.back_bracket[back_dub[dis]]])
                cur+=1
                dis+=1
            elif back_dub[dis] != back_dub[cur]+1 :
                cur=dis
                dis += 1
            else :
                cur+=1
                dis+=1
        
        cur=0
        dis=1
        while(cur<len(self.dub)-1) :
            if self.dub[cur][-1] == self.dub[cur+1][0] :
                del self.dub[cur][-1]
                self.dub[cur].append(self.dub[cur+1][0])
                self.dub[cur].append(self.dub[cur+1][1])
                del self.dub[cur+1]
                

            else :
                cur+=1
                continue

        for i in range(0, len(self.dub)) :
            self.back_bracket.append(self.dub[i])
            for j in range(0, len(self.dub[i])) :
                self.back_bracket.remove(self.dub[i][j])
                

        self.bracket_broking()

    def bracket_broking(self, ) :
        pass
    
    def nan_claculations(self, num1, num2, ope) :
        calculations = {
            "+" : num1+num2,
            "-" : num1-num2,
            "*" : num1*num2,
            "/" : num1/num2,
            "**" : num1**num2,
        }
        return calculations[ope]
        

if __name__ == "__main__" :
    # get_input = str(input(">> "))
    get_input = "12+3+(4+8)+(80+20)+40+50+(((((2*4)+(30+40)))))"
    myObj = CalculatorProgramme(get_input)
    if not(myObj.checking_numbers()) :
        # get_input = str(input(">> "))
         get_input = "12+3+(4+8)+(80+20)+40+50+(((((2*4)+(30+40)))))"

