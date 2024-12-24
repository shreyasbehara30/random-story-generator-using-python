import random

def generate_story():
    
    subjects = ["A wizard", "A knight", "An alien", "A detective", "A pirate","A technician"]
    verbs = ["found", "fought", "discovered", "explored", "saved","fixed bugs"]
    objects = ["a hidden treasure", "a mysterious cave", "an ancient spell", "a powerful artifact", "a lost kingdom","with help of a fast computer"]
    places = ["in the forest", "on a distant planet", "under the ocean", "in a haunted castle", "in a secret lab","in a major corporation"]
    ending =["returned to palace","died like a hero","lived a peaceful life","never saw anyone","became a killer"]
    # Randomly select components
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    place = random.choice(places)
    end = random.choice(ending)

   
    story = f" once upon a time there was {subject} he {verb} with {obj}  {place} and at last {end}"
    return story


if __name__ == "__main__":
    
    story = generate_story()
    print("\nHere is your story:")
    print(story)
