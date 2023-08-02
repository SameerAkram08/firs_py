import os

class Clear:
    def Create(self):
        if (not os.path.exists("clear clusster prog")):
            os.mkdir("clear clusster prog")
        for i in range(0,5):
            os.mkdir(f"clear clusster prog/vsfs {i+1}")

    def rename(self):
        for i in range (0,5):
            
            os.rename(f"clear clusster prog/vsfs {i+1}", f"clear clusster prog/{i+1}.png")

obj = Clear()
# obj.Create()
obj.rename()
