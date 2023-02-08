using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System;
using System.Collections.Generic;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.IO;

using Newtonsoft.Json;



namespace RobotController
{

    public class ProgStart
    {

        public static void StartProcess(string path, string argu)
        {
            var p = new Process
            {
                StartInfo =
     {
         FileName = "C:\\Windows\\system32\\cmd.exe",
         WorkingDirectory = path,
         Arguments = argu,
     }
            };

            p.Start();


        }

    }

}

    



  
