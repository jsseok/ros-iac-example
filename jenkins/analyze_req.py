def mobility_feature_extraction(text):
    # TODO: Implement actual natural language processing to extract features
    # For now, we'll use a simple check for specific words
    features = []
    if "localization" in text.lower():
        features.append("localization")
    if "image segmentation" in text.lower():
        features.append("image segmentation")
    return features

def main():
    # Read the user requirements file
    with open("jenkins/user_requirement.txt", "r") as file:
        user_requirements = file.read()

    # Extract features
    extracted_features = mobility_feature_extraction(user_requirements)

    # Write the extracted features to a file
    with open("jenkins/artifact/list_of_features.txt", "w") as file:
        for feature in extracted_features:
            file.write(f"{feature}\n")

if __name__ == "__main__":
    main()