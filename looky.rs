use io::SeekFrom;
use std::env;
use std::fs::{File, metadata};
use std::io;
use std::io::prelude::*;


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
        let the_file = &args[2];
        let the_number = &args[1].parse::<u64>().expect("No parse 1");
        let the_meta = metadata(the_file);
        let file_length = the_meta.expect("Bad 1").len();

        if file_length >= *the_number {
            print_number_bytes(&args[1], &args[2]);
        }
        else { 
            println!("File is smaller than {} bytes", the_number);
            println!("It's {} bytes long", file_length);
            println!("For help type looky -h");
        }
    }

    else if args.len() == 4 && string_digit(&args[1]) && string_digit(&args[2]) && !string_digit(&args[3])
    {
        let the_file = &args[3];
        let end_num = &args[2].parse::<u64>().expect("No parse 2");

        let the_meta = metadata(the_file);
        let file_length = the_meta.expect("Bad 2").len();

        if file_length >= *end_num {
            print_start_end(&args[1], &args[2], &args[3]);
        }
        else {
            println!("File is smaller than your endpoint {}", end_num);
            println!("File is {} bytes long", file_length);
            println!("For help type looky -h");
        }
    }

    else if args.len() == 4 && &"last" == &args[1] && string_digit(&args[2]) && !string_digit(&args[3])
    {
        let the_file = &args[3];
        let the_diff = &args[2].parse::<u64>().expect("No parse 3");
        let the_meta = metadata(the_file);
        let file_length = the_meta.expect("Bad 3").len();

        let the_start = file_length - the_diff;
        print_start_end(&the_start.to_string(), &file_length.to_string(), &args[3]);
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
    stdout.write_all(b"\tE.G. looky 30 60 the_file\n").expect("No write*9");
    stdout.write_all(b"\tTo get the last bytes of a file,\n").expect("no write*10");
    stdout.write_all(b"\tType looky last number file\n").expect("no write*11");
    stdout.write_all(b"\tE.G. looky last 50 the_file\n\n").expect("no write*12");
}
