import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class SimpleWebHandler(BaseHTTPRequestHandler):
    """
    Handle GET and POST requests for the E-commerce project.
    """

    def do_GET(self):
        """
        Handle GET requests by returning the Contacts page.
        As per Task 2, it should return 'Contacts' page for *any* GET request.
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Path to the contacts template
        template_path = os.path.join(os.path.dirname(__file__), 'templates', 'contacts.html')
        
        # Read the HTML content using open() as required
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            self.wfile.write(b"<h1>404 - Template Not Found</h1>")

    def do_POST(self):
        """
        Handle POST requests and print received data to the console.
        """
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)

        # Print all received data to the console as required
        print("\n[POST DATA RECEIVED]")
        for key, value in parsed_data.items():
            print(f"{key}: {', '.join(value)}")
        print("-" * 20)

        # Send response back to user
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"<h1>Success!</h1><p>Data received and printed to console.</p><a href='/'>Go Back</a>")

def run(server_class=HTTPServer, handler_class=SimpleWebHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting simple web server on port {port}...")
    print(f"Server is running at http://localhost:{port}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == '__main__':
    run()
