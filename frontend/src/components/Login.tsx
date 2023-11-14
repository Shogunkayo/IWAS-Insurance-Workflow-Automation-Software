import axios from 'axios';
import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { ToastContainer, ToastOptions, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { setOpen, setUser } from '../redux/features/authSlice';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const dispatch = useDispatch()

    const toast_error_config: ToastOptions = {
        position: 'top-center',
        autoClose:5000,
        theme:'light',
        type:'error'
    }

    const handleLogin = () => {
        if (email === '' || password === '')
            return toast("Please enter both email and password.", toast_error_config)
        
        axios.post("http://localhost:5000/login", JSON.stringify({email, password}), {headers: {'Content-Type': 'application/json'}})
            .then(response => {
                if (!response.data || !response.data.token || !response.data.uid)
                    return toast("Server error. Please try later", toast_error_config)
                
                dispatch(setUser({'token': response.data.token, 'uid': response.data.uid, 'email': email}))
                dispatch(setOpen(false)) 
            })
            .catch(error => {
                console.log(error)
            })
        

        setEmail('');
        setPassword('');
    };

    return (
        <div className="flex items-center justify-center">
            <div className="bg-white p-8 relative rounded shadow-md w-96">
                <h1 className="text-3xl font-bold text-center mb-6">Login</h1>
                <div className="mb-4">
                    <label htmlFor="email" className="block text-gray-700"><span className="text-secondary">*</span> Email:</label>
                    <input
                        type="email"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="w-full p-2 border rounded mt-1"
                    />
                </div>
                <div className="mb-4">
                    <label htmlFor="password" className="block text-gray-700"><span className="text-secondary">*</span> Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="w-full p-2 border rounded mt-1"
                    />
                </div>
                <div className="text-center">
                    <button
                        type="button"
                        onClick={handleLogin}
                        className="btn-primary w-1/2 mx-auto"
                    >
                        Login
                    </button>
                </div>
            </div>
            <ToastContainer></ToastContainer>
        </div>
    );
};

export default Login;

