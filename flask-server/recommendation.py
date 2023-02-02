#recommendation algorithm for glasses frame based on detected face shape



recommendation = {'triangle': ['rectangle', 'browline', 'oval', 'aviators', 'geometric', 'wrap'],
                  'heart' : ['rectangle', 'aviators', 'geometric', 'wrap'],
                  'diamond' : ['oval', 'aviators', 'round', 'wrap'],
                  'round' : ['rectangle', 'square', 'aviators', 'wrap'],
                  'oblong' : ['classic wayframe', 'browline', 'oval', 'aviators', 'round', 'geometric', 'wrap'],
                  'oval' : ['rectangle', 'square', 'classic wayframe', 'browline', 'aviators', 'geometric', 'wrap'],
                  'square' : ['classic wayframe', 'browline', 'oval', 'aviators', 'round', 'wrap']
                  }

# face_shape - string
# void function

def getRecommendation(face_shape):
    print('Face shape is: ' + face_shape)
    recommendation_list = recommendation[face_shape]
    print('Recommended glasses frame is:')
    return recommendation_list
#    for item in recommendation_list:
#        print(item)
        
# getRecommendation('oval')