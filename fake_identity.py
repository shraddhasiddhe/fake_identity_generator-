import random
import json

def genrate_name():
    first_name = ["shraddha", "shreya", "shruti", "mohit","shubham", "shrayu"]
    last_name = ["siddhe", "Patil", "mehat", "purohit"]
    return f"{random.choice(first_name)} {random.choice(last_name)}"

def genrate_job():
    job = ["Techcontentcreator", "Yogateacher", "AI engineer", "Software Developer", "Chef", "Business", "Civil"]
    return random.choice(job)

def genrate_location():
    location = ["mumbai", "delhi", "solapur", "pune", "nasik"]
    return random.choice(location)

def genrate_age():
    return random.randint(18, 40)

def generate_email(name):
    clean = name.lower().replace(" ", ".")
    return f"{clean}{random.randint(10, 99)}@gmail.com"

def genrate_identity():
    name = genrate_name()
    job = genrate_job()
    location = genrate_location()
    age = genrate_age()
    email = generate_email(name)

    return {
        "name": name,
        "job": job,
        "location": location,
        "age": age,
        "email": email
    }

# Step 2: Ask user how many identities to generate
def main():
    try:
        count = int(input("How many fake identities do you want to generate? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    identities = []
    for _ in range(count):
        identities.append(genrate_identity())

    print("Here are your fake identities:")
    for identity in identities:
        print(identity)

    # Step 3: Ask if user wants to save to JSON
    save = input("Do you want to save them to a JSON file? (yes/no): ").lower()
    if save == "yes":
        with open("fake_identities.json", "w") as f:
            json.dump(identities, f, indent=4)
        print("✅ Identities saved to fake_identities.json")

if __name__ == "__main__":
    main()
