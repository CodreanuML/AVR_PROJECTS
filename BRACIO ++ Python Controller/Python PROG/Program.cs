// See https://aka.ms/new-console-template for more information
using System;
using System.Diagnostics;


ProgramRun.RunScript OpenPython = new ProgramRun.RunScript();
OpenPython.StartProcess();




namespace ProgramRun{
    class RunScript { 

        public void StartProcess()
{
            var p = new Process
            {
                StartInfo =
     {
         FileName = "C:\\Windows\\system32\\cmd.exe",
         WorkingDirectory = @"C:\Users\mcodrea2\Desktop\PROIECTE\Arduino\Bracio\PythonPROG\PythonWrapper",
         Arguments = "/c gui_tkinter.py"
     }
            };

            p.Start();


        }
    }

}





