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
            NotImplementedError
                
    def check_operators(self, ):
        operators = ["+", "-", "*", "/", "//", "**"]
        self.algo_operator = ["(", ")"]
        if "(" in self.user :
            self.bracketing(self.algo_operator)

        else :
            self.nan_claculations()

    def bracketing(self, ope):
        fow_bracket = []
        back_bracket = []
        for f_b in range(0, len(self.user)-1) :
            if self.algo_operator[0] in self.user[f_b] :
                fow_bracket.append(f_b)
            if  self.algo_operator[1] in self.user[f_b] :
                back_bracket.append(f_b)

        cur=0
        dis=1
        back_dub = []
        back_bracket.append(40)
        while(dis<len(back_bracket)) :
            if back_bracket[dis] == back_bracket[cur]+1 :
                print(dis)
                cur+=1
                dis+=1
            
            else :
                cur+=1
                dis+=1
    def converter(self, lenth, id) :
        res = (lenth-(id))*-1
        return res
    
    def catogorizing(self,) :
        cur=0
        dis=1
        das=0 
        cato = []
        while(dis < len(self.user_n)) :
            if self.ope in self.user_n[dis] :
                cato.append(self.user_n[cur:dis+1])
                cur = dis+1
                dis = dis+2
            else :
                dis += 1
        print(cato)
        return cato

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
    get_input = "12+3+(4+8)+(80+20)+40+50+((2*4)+(30+40))"
    myObj = CalculatorProgramme(get_input)
    if not(myObj.checking_numbers()) :
        # get_input = str(input(">> "))
        get_input = "12+3+(4+8)+(80+20)+40+50+((2*4)+(30+40))"

