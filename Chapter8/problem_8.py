def get_param(string):

    perm = []

    if string is None:
        raise Exception("No string provided")

    if len(string) == 0:
        perm.append(" ")

        return perm

    first = string[0]
    remaining = string[1:]

    words = get_param(remaining)
   

    for k in words: 

        index = 0 

        for letter in k:

            s = charAt(k, first, index)

            
            perm[s] = s 
            index += 1 

    return perm


def charAt(word, first, index):

    start = word[:index]
    end = word[index:]

    return start+first+end



print(get_param("maah"))






