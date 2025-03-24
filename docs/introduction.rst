Introduction
============

This is an example of a documentation page written in reStructuredText (RST).

.. raw:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <style>
        /* Style for centering and making iframe look nice */
        .iframe-container {
          display: flex;
          justify-content: center;
          align-items: center;
          padding: 20px;
          min-height: 50vh;  /* Ensures the iframe is centered vertically but takes up less space */
          background-color: #f7f7f7; /* Soft background for the page */
        }

        iframe {
          width: 80%;  /* Adjust the width as a percentage */
          max-width: 800px; /* Maximum width of the iframe */
          height: 500px; /* Fixed height for the iframe */
          border: none;
          border-radius: 10px; /* Rounded corners */
          box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Soft shadow around the iframe */
          transition: transform 0.3s ease;
        }

        iframe:hover {
          transform: scale(1.02); /* Slight zoom on hover */
        }
      </style>
      <title>Embedded Draw.io Diagram</title>
    </head>
    <body>
      <div class="iframe-container">
        <iframe src="https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=xdg-uml.drawio&dark=auto#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1jOOYsrMjI29D81mtemU_79hzjtlid_aa%26export%3Ddownload"></iframe>
      </div>
    </body>
    </html>
