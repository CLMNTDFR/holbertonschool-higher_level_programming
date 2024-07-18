#!/usr/bin/python3


def generate_invitations(template, attendees):
    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict)
                                                  for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Check if the template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Create a copy of the template to replace placeholders
        invitation = template[:]

        # Replace placeholders with attendee's data or "N/A" if data is missing
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") or "N/A"
            invitation = invitation.replace(f"{{{key}}}", value)

        # Write the invitation to an output file
        output_filename = f"output_{idx}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)


# Example Main File to Test the Program
if __name__ == "__main__":
    # Read the template from a file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference",
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None,
         "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)