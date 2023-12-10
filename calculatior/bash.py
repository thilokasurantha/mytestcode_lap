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
        self.idx_s = 0
        self.idx_e = -1

        while (self.idx_s<=len(self.user)-1) :
            if (self.user[self.idx_s]==self.ope[0]) :
                self.idx_s
                break
            else :
                self.idx_s += 1

        while (self.idx_e>=len(self.user)*-1) :
            if (self.user[self.idx_e]==self.ope[1]) :
                self.idx_e_re = self.converter(len(self.user)*-1, self.idx_e)
                break

            else :
                self.idx_e = self.idx_e+(-1)
                
            
    def converter(self, lenth, id) :
        res = (lenth-(id))*-1
        return res

    def nan_claculations(self,) :
        print("er3")


if __name__ == "__main__" :
    # get_input = str(input(">> "))
    get_input = "12+3+(12+3+4/5-(12+4))"
    myObj = CalculatorProgramme(get_input)
    if not(myObj.checking_numbers()) :
        # get_input = str(input(">> "))
        get_input = "12+3+(12+3+4/5-(12+4))"
        dsdsadsdd
        gdfgjfdgfdklgljkf

