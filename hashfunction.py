
class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """

    def hashcode(self,key,HASH_SIZE):
        ans = 0
        for x in key:
            ans = (ans*33 + ord(x))%HASH_SIZE
        return ans