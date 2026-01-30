def minNumberOfHours(initialEnergy, initialExperience, energy, experience):
    hoursTrain = 0
    totalEnergy = 0
    totalExperience = initialExperience
    for i in energy:
        totalEnergy += i
        
    for i in experience:
        if totalExperience <= i:
            hoursTrain += (i - totalExperience + 1)
            totalExperience += i - totalExperience + 1
        totalExperience += i
        
    print(hoursTrain)
    if initialEnergy <= totalEnergy:
        hoursTrain += (totalEnergy - initialEnergy + 1)
    
    return hoursTrain
        
    # sumEnergy = 0
    # maxEx = max(experience)
    
    # sumEx = 0
    # for i in energy:
    #     sumEnergy += i
    # for i in experience:
    #     if i == maxEx:
    #         break
    #     sumEx += i
    # return sumEnergy, sumEx, maxEx
    
    return hoursTrain
        
                
            
print(minNumberOfHours(initialEnergy = 5, initialExperience = 1, energy = [1,3,3], experience =[1,3,7]))