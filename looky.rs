use io::SeekFrom;
use std::env;
use std::fs::File;
use std::io;
use std::io::prelude::*;
use std::io::Write;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() == 1 { 

        let mut stdout = io::stdout().lock();
        stdout.write_all(b"\n\tFor help type looky -h\n\n").expect("No write1");
    }

    else if args.len() == 2 && args[1] == "-h" {
        help_func();
    }

    else if args.len() == 2 && &args[1] == "-v" {
        let mut stdout = io::stdout().lock();
        stdout.write_all(b"\n\tVersion 0.1\n\n").expect("No write2");

    }

    else if args.len() == 3 &&  string_digit(&args[1]) && !string_digit(&args[2]) {
        print_number_bytes(&args[1], &args[2]);
    }

    else if args.len() == 4 && string_digit(&args[1]) && string_digit(&args[2]) && !string_digit(&args[3])
    {
        print_start_end(&args[1], &args[2], &args[3]);
    }

    else { 
        let mut stdout = io::stdout().lock();
        stdout.write_all(b"\n\tFor help type looky -h\n").expect("No write3");

    }

}

fn string_digit(my_string: &String) -> bool {
    for c in my_string.chars() {
        if !c.is_digit(10) {
            return false;
        }
    }
    return true;
}

fn print_number_bytes(number_byte: &String, the_file: &String) {
    let a_num = number_byte.parse::<usize>().unwrap();
    let mut f = File::open(&the_file).expect("No1");
    let start = 0;
    let count = a_num;
    f.seek(SeekFrom::Start(start)).expect("No2");
    let mut buf = vec![0; count];
    f.read_exact(&mut buf).expect("No3");

    let mut stdout = io::stdout().lock();
    stdout.write_all(&buf).expect("No write4");
    stdout.write_all(b"\n").expect("No write5");

}

fn print_start_end(number_byte1: &String, number_byte2: &String, the_file: &String)
{
    let a_num1 = number_byte1.parse::<u64>().unwrap();
    let a_num2 = number_byte2.parse::<usize>().unwrap();
    let mut f = File::open(&the_file).expect("No1");
    let start = a_num1;
    let u_num1 = a_num1 as usize;
    let count = a_num2 - u_num1;
    f.seek(SeekFrom::Start(start)).expect("No2");
    let mut buf = vec![0; count];
    f.read_exact(&mut buf).expect("No3");

    let mut stdout = io::stdout().lock();
    stdout.write_all(&buf).expect("No write6");
    stdout.write_all(b"\n").expect("No write7");
}

fn help_func() {

    let mut stdout = io::stdout().lock();
    stdout.write_all(b"\n\tType looky -h for help.\n").expect("No write*1");
    stdout.write_all(b"\tType looky -v for version.\n").expect("No write*2");
    stdout.write_all(b"\tFor number of bytes to display,\n").expect("No write*3");
    stdout.write_all(b"\tstarting from begining of file,\n").expect("No write*4");
    stdout.write_all(b"\tType looky number of bytes and file.\n").expect("No write*5");
    stdout.write_all(b"\tE.G. looky 50 the_file\n").expect("No write*6");
    stdout.write_all(b"\tTo specify start stop and file,\n").expect("No write*7");
    stdout.write_all(b"\tType looky number number file\n").expect("No write*8");
    stdout.write_all(b"\tE.G. looky 30 60 the_file\n\n").expect("No write*9");
}
