from reportlab.lib.units import cm, mm
from reportlab.pdfgen.canvas import Canvas

# Function to draw a single sticker with the given room number
def draw_sticker(canvas, room_number, x, y):
    # Set the font and font size
    canvas.setFont('Helvetica', 12)
    # Draw the "Room" text on the first line
    canvas.drawString(x+1*mm, y+15*mm, "Room")
    # Draw the room number on the second line
    canvas.drawString(x+6*mm, y+10*mm, str(room_number))

# Function to generate the PDF with the stickers
def generate_stickers(start, end, filename):
    # Calculate the size of each sticker
    sticker_width = 20*mm
    sticker_height = 20*mm
    # Calculate the spacing between stickers
    sticker_spacing = 2*mm
    # Calculate the margin around the stickers
    margin = 5*mm
    # Calculate the width of the page
    page_width = 10.2*cm
    # Calculate the height of the page
    page_height = (end - start + 1) * (sticker_height + sticker_spacing) + 2 * margin
    # Calculate the x and y position of the top left corner of the first sticker
    x = margin
    y = page_height - margin - sticker_height
    # Create a new PDF with ReportLab
    canvas = Canvas(filename, pagesize=(page_width, page_height))
    # Iterate over the range of room numbers in reverse order
    for room_number in range(end, start-1, -1):
        # Draw a sticker with the current room number
        draw_sticker(canvas, room_number, x, y)
        # Increment the x position for the next sticker
        x += sticker_width + sticker_spacing
        # If we have reached the end of the row, move to the next row
        if x + sticker_width > page_width - margin:
            x = margin
            y -= sticker_height + sticker_spacing
        # If we have reached the top of the page, start a new page
        if y < margin:
            canvas.showPage()
            x = margin
            y = page_height - margin - sticker_height
    # Save the PDF
    canvas.save()

# Prompt the user to input the start and end room numbers
start = int(input("Enter the start room number: "))
end = int(input("Enter the end room number: "))

# Generate the PDF with the stickers
generate_stickers(start, end, f"room_stickers_{start}_{end}.pdf")
