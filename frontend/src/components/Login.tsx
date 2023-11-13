import { useState } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = () => {
        if (email === '' || password === '')
            return toast("Please enter both email and password.", {position: 'top-center', autoClose:5000, theme:'light', type:"error"})

        console.log('Email:', email);
        console.log('Password:', password);
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

