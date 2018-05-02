res = 0
for p1 in range(201):
    for p2 in range((200 - p1) / 2 + 1):
        for p5 in range((200 - p1 - p2*2) / 5 + 1):
            for p10 in range((200 - p1 - p2*2 - p5*5) / 10 + 1):
                for p20 in range((200 - p1 - p2*2 - p5*5 - p10*10) / 20 + 1):
                    for p50 in range((200 - p1 - p2*2 - p5*5 - p10*10 - p20*20) / 50 + 1):
                        for f1 in range((200 - p1 - p2*2 - p5*5 - p10*10 - p20*20 - p50*50) / 100 + 1):
                            if p1 + p2*2 + p5*5 + p10*10 + p20*20 + p50*50 + f1*100 == 200:
                                res += 1

print res+1