import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_clowns, get_all_completions, get_all_requests
from views import delete_request
from views import create_request



# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server"""

    # Here's a class function

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        """Handles GET requests to the server"""
        response = {}
        (resource, id) = self.parse_url(self.path)
        if resource == "clowns":
            if id is not None:
                response = get_single_clown(id)
            else:
                response = get_all_clowns()
        if resource == "requests":
            if id is not None:
                response = get_single_request(id)
            else:
                response = get_all_requests()
        if resource == "completions":
            if id is not None:
                response = get_single_completion(id)
            else:
                response = get_all_completions()
        if response is not None:
            # Set the response code to 'Ok'
            self._set_headers(200)
        else:
            self._set_headers(404)
            response = {"message": f"{resource} {id} is currently unavailable"}
        # Send a JSON formatted string as a response
        self.wfile.write(json.dumps(response).encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        """Handles POST requests to the server"""

        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len)

        (resource, id) = self.parse_url(self.path)
        
        response = None

        if resource == "requests":
            response = create_request(post_body)

        # Encode the new animal and send in response
        
        self.wfile.write(json.dumps(response).encode())



    #^DELETE REQUEST
    def do_DELETE(self):
        """Handles DELETE requests to the server"""
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single reservation from the list
        if resource == "requests":
            delete_request(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())




    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers"""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
        self.send_header(
            "Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Accept"
        )
        self.end_headers()

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None
        try:
            id = int(path_params[2])
        except IndexError:
            pass  
        except ValueError:
            pass  
        return (resource, id)  


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class"""
    host = ""
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
