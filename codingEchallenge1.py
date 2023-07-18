'''
Você recebe dois arrays inteiros nums1e nums2, classificados em ordem não decrescente , e dois inteiros me n, 
representando o número de elementos em nums1e nums2 respectivamente.
Mescle nums1 e nums2em uma única matriz classificada em ordem não decrescente .
A matriz classificada final não deve ser retornada pela função, mas, em vez disso, ser armazenada dentro da matriz nums1 . 
Para acomodar isso, nums1tem um comprimento de m + n, 
onde os primeiros melementos denotam os elementos que devem ser mesclados e 
os últimos nelementos são definidos como 0e devem ser ignorados. nums2 tem um comprimento de n.
'''

def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    self.nums1 = nums1
    self.nums2 = nums2
    del nums1[m:len(nums1)]
    nums1.extend(nums2)
    nums1.sort()
    return nums1

merge([1,2,3,0,0,0], 3, [2,5,6], 3)