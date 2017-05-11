x = [1,10,1,10, 'fuck', 'yeah']

# def draw_stars(x):
#     for i in range(0, len(x)):
#         s=0
#         print i
#         while s < x[i]:
#             print '*',
#             s+=1
#         print ' '
#     return 'Enjoy the stars'
#
#
# print draw_stars(x)



def draw_stars(x):
    for i in range(0, len(x)):
        if type(x[i])==int:
            s=0
            while s < x[i]:
                print '*',
                s+=1
            print ' '
        elif type(x[i])==str:
            print x[i][0]*len(x[i])


draw_stars(x)
