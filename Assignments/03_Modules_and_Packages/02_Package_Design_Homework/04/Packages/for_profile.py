profiles=[]

def profile(name,**kwargs):
    profiles.append({
        "name":name,
        **kwargs
    })
    print("Details updated...")
    for k in range(len(profiles)):
        for i,j in profiles[k].items():
            print(i,"\t",j)
