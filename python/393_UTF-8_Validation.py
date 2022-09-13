class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def int2bin(num):
            ans = ""
            for i in range(8):
                ans = str(num%2)+ans
                num = num//2
            return ans
        
        binary_str = [int2bin(num) for num in data]
        
        pointer = 0
        while pointer<len(binary_str):
            current_str = binary_str[pointer]
            if current_str[0]=="0":
                pointer+=1
                continue
                
            if current_str[:3]=="110":
                if pointer+1>=len(binary_str):
                    return False
                for i in range(1):
                    pointer+=1
                    current_str = binary_str[pointer]
                    if current_str[:2]!="10":
                        return False
                pointer+=1
                continue
                
            if current_str[:4]=="1110":
                if pointer+2>=len(binary_str):
                    return False
                for i in range(2):
                    pointer+=1
                    current_str = binary_str[pointer]
                    if current_str[:2]!="10":
                        return False
                pointer+=1
                continue
            
            if current_str[:5]=="11110":
                if pointer+3>=len(binary_str):
                    return False
                for i in range(3):
                    pointer+=1
                    current_str = binary_str[pointer]
                    if current_str[:2]!="10":
                        return False
                pointer+=1
                continue
                
            return False
                
        return True
            