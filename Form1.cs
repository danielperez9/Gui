using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;
//using IronPython.Hosting;

namespace UI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void btnclose_Click(object sender, EventArgs e)
        {
            MessageBox.Show("", "This Winodow will be closing");
            Application.Exit();
        }

        private void btnpy_Click(object sender, EventArgs e)
        {
           
            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.Arguments = "C:\\workspaces\\side projects-\\Argonnecode\\andom.py";
            proc.StartInfo.RedirectStandardOutput = true;
            proc.StartInfo.UseShellExecute = true;
            proc.StartInfo.CreateNoWindow = false;
            string result = "";
            //passing file through parameters
            
            proc.Start();
            Console.WriteLine(result);
            Console.ReadKey();
            







        }
    }
}
