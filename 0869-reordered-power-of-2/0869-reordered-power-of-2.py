from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        n_str = str(n)
        n_list = [int(_) for _ in n_str]

        n_list_sorted = sorted(n_list)
        n_list_reversed = sorted(n_list, reverse =True)

        freq_n = Counter(n_list)
        

        smallest_n = int(''.join(str(l) for l in n_list_sorted))
        n_bit_length = smallest_n.bit_length() - 1 

        largest_n = int(''.join(str(l) for l in n_list_reversed))
        n_bit_length_largest = largest_n.bit_length()

        for k in range(n_bit_length ,  n_bit_length_largest):

            power_2_n_hash = Counter([int(m) for m in str(2 ** k )]) 
            
            if power_2_n_hash == freq_n: 

                return True 
                
        return False