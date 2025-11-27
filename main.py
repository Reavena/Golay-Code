import encoding as en
import decoding as de
import vector_processor as v
import text_processor as t
import image_processor as i

def main():
    while True:
        print("\n=== Golay Code Program ===")
        print("1. Process Vector")
        print("2. Process Text")
        print("3. Process Image")
        print("4. Exit")
        
        choice = input("Choose option (1-4): ").strip()
        
        if choice == "1":
            v.process_vector()
        elif choice == "2":
            t.process_text()
        elif choice == "3":
            i.process_image()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()