def extract_5_letter_words(input_filename, output_filename):
    with open(input_filename, 'r') as infile:
        words = infile.read().split()
        words.sort()
    # five_letter_words = [word for word in words if len(word) == 5]
    x = 0;
    with open(output_filename,'w') as outfile:
        outfile.write("{")
        for word in words:
            outfile.write("\"")
            outfile.write(word)
            outfile.write("\"")
            outfile.write(",")
            print(word)
            x = x+1
        outfile.write("}")

    print("Words : ",x)

    # with open(output_filename, 'w') as outfile:
        # outfile.write('\n'.join(five_letter_words))

# Example usage:
input_file = 'gitwords.txt'  # Replace with your input file name
output_file = 'gitoutput.txt'  # Replace with your desired output file name
extract_5_letter_words(input_file, output_file)