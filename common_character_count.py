def commonCharacterCount(s1, s2):

    # Get a list of individual characters is in s1
    unique_characters = list(set(s1))

    common_count = 0
    for character in unique_characters:
        common_count += min(s1.count(character), s2.count(character))

    return common_count