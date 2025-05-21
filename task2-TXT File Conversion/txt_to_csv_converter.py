      
#my imports        
import pandas as pd

def convert_txt_to_csv(txt_file_path, csv_file_path, delimiter=' '):  # Changed default to space
    """
    Convert space-delimited text file to CSV
    """
    try:
        # check if  with space delimiter and quote handling
        df = pd.read_csv(txt_file_path, delimiter=delimiter, quotechar='"', skipinitialspace=True)
        
        # try and  Save to CSV
        df.to_csv(csv_file_path, index=False)
        
        #if yes else do opposite
        print(f"Successfully converted {txt_file_path} to {csv_file_path}")
        return True
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        return False

# the paths on my local machine to save
if __name__ == "__main__":
    input_file = "/home/thembajsph/Videos/Alignd - Analytics Engineering Assessment final/task2-TXT File Conversion/health_products.txt"
    output_file = "/home/thembajsph/Videos/Alignd - Analytics Engineering Assessment final/task2-TXT File Conversion/health_products.csv"
    
    
    # use the space delimeter
    convert_txt_to_csv(input_file, output_file, delimiter=' ')